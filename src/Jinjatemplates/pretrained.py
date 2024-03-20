
# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision import models, transforms
from torchvision.transforms import v2
from torch.optim import lr_scheduler


# initiallization
BATCH_SIZE = 64
EPOCHS = 1
TRAIN_SPLIT = 0.75
VAL_SPLIT = 0.15
TEST_SPLIT = 0.1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(weights='DEFAULT')

for name, param in model.named_parameters():
    # print(param[0])
    print(param.shape)
    batch = param.shape[0]
    channels = param.shape[1]
    height = param.shape[2]
    width = param.shape[3]

    # print(batch)
    break
# print(model.named_parameters()[0])
# Get the input size of the model
# print(model.__init__)
# input_size = tuple(model.children().__next__().weight.size()[2:])
# channels = model.children().__next__().weight.size()[1]

for param in model.parameters():
    param.requires_grad = False
print(height, width)
transform = transforms.Compose([
    v2.Resize((224, 224)),
    v2.Grayscale(num_output_channels=channels),  # Convert images to RGB format
    # Convert images to PyTorch tensors
    v2.ToImage(), v2.ToDtype(torch.float32, scale=True)
])
train_dataset = mnist.MNIST(root='E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/data/MNIST/train',
                            train=True, download=True, transform=transform)
test_dataset = mnist.MNIST(root='E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/data/MNIST/test',
                           train=False, download=True, transform=transform)
train_dataloader = DataLoader(
    train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_dataloader = DataLoader(
    test_dataset, batch_size=BATCH_SIZE, shuffle=False)
loss_fn = nn.CrossEntropyLoss()
class_names = train_dataset.classes


num_ftrs = model.fc.in_features
# Here the size of each output sample is set to 2.
# Alternatively, it can be generalized to ``nn.Linear(num_ftrs, len(class_names))``.
model.fc = nn.Linear(num_ftrs, len(class_names))

model = model.to(device)

# Observe that all parameters are being optimized
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Decay LR by a factor of 0.1 every 7 epochs
exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)


# Parameters of newly constructed modules have requires_grad=True by default


# optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

for e in range(0, EPOCHS):
    # print(EPOCHS)
    # set the model in training mode
    model.train()
    # initialize the total training and validation loss
    totalTrainLoss = 0
    totalValLoss = 0
    # initialize the number of correct predictions in the training and validation step
    trainCorrect = 0
    valCorrect = 0
    # loop over the training set
    for (x, y) in train_dataloader:
        # print("hamada")
        # send the input to the device
        (x, y) = (x.to(device), y.to(device))
        # perform a forward pass and calculate the training loss
        pred = model(x)
        loss = loss_fn(pred, y)
        # zero out the gradients, perform the backpropagation step, and update the weights
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # add the loss to the total training loss so far and calculate the number of correct predictions
        totalTrainLoss += loss
        trainCorrect += (pred.argmax(1) == y).type(
            torch.float).sum().item()
    model.eval()
    print(trainCorrect)


with torch.no_grad():
    model.eval()
    # initialize a list to store our predictions
    preds = []
    testCorrect = 0
    for (x, y) in test_dataloader:
        x = (x.to(device))
        y = (y.to(device))

        pred = model(x)
        preds.extend(pred.argmax(axis=1).cpu().numpy())
        testCorrect += (pred.argmax(1) == y).type(
            torch.float).sum().item()
        print(testCorrect)


# calculate the training, validation, and test accuracy
trainAccuracy = trainCorrect / len(train_dataloader.dataset)
testAccuracy = testCorrect / len(test_dataloader.dataset)

print("Train Accuracy:", trainAccuracy)
print("Test Accuracy:", testAccuracy)
tensors = torch.jit.script(model)
tensors.save(
    "E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/data/result/model3.pt")
