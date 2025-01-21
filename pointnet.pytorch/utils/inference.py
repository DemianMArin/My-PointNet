import argparse
import os
import torch
# import torch.nn.parallel
import torch.optim as optim
# import torch.utils.data
from pointnet.dataset import ModelNetDataset
from pointnet.model import PointNetCls
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument(
    '--batchSize', type=int, default=32, help='input batch size')
parser.add_argument(
    '--num_points', type=int, default=2500, help='input batch size')
parser.add_argument(
    '--workers', type=int, help='number of data loading workers', default=4)
parser.add_argument(
    '--test_file',  default='test_one', help="file for testing")
parser.add_argument('--feature_transform', action='store_true', help="use feature transform")


opt = parser.parse_args()
print(opt)

test_dataset = ModelNetDataset(
    root='/home/vanttec/PointNet/Convert2ply/test/',
    split=opt.test_file,
    npoints=opt.num_points,
    data_augmentation=False)

testdataloader = torch.utils.data.DataLoader(
    test_dataset,
    batch_size=opt.batchSize,
    shuffle=True,
    num_workers=int(opt.workers))

num_classes = len(test_dataset.classes)
classifier = PointNetCls(k=num_classes, feature_transform=opt.feature_transform)

classifier.load_state_dict(torch.load('/home/vanttec/PointNet/pointnet.pytorch/utils/cls/cls_model_0.pth'))

optimizer = optim.Adam(classifier.parameters(), lr=0.001, betas=(0.9, 0.999))
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.5)
classifier.cuda()

print(f"Starting Inference \n")
total_correct = 0
total_correct3 = 0
total_testset = 0
for i,data in tqdm(enumerate(testdataloader, 0)):
    points, target = data
    target = target[:, 0]
    points = points.transpose(2, 1)
    points, target = points.cuda(), target.cuda()
    classifier = classifier.eval()
    pred, _, _ = classifier(points)
    pred_choice = pred.data.max(1)[1] # First pred
    top_values = torch.topk(pred, 3)[1] # First 3 pred
    correct = pred_choice.eq(target.data).cpu().sum()
    correct1 = top_values[:,0].eq(target.data).cpu().sum()
    correct2 = top_values[:,1].eq(target.data).cpu().sum()
    correct3 = top_values[:,2].eq(target.data).cpu().sum()
    # print(f"\nTarget: {target.data}")
    # print(f"\nTop val: \n{top_values}")
    # print(f"\nCorrect: {correct1} {correct2} {correct3}") 
    # print(f"\nEnd iter")
    total_correct += correct.item()
    total_correct3 += (correct1.item() + correct2.item() + correct3.item())
    total_testset += points.size()[0]
print("final accuracy {}".format(total_correct / float(total_testset)))
print("final 3 accuracy {}".format(total_correct3 / float(total_testset)))
