import torch
import torchvision.models as models
import matplotlib.pyplot as plt

# Load model
model = models.segmentation.fcn_resnet50(pretrained=True)
model.eval()

# Dummy image
input_image = torch.rand(1, 3, 224, 224)

# Predict
output = model(input_image)['out']
mask = torch.argmax(output.squeeze(), dim=0).detach().numpy()

# Display
plt.imshow(mask)
plt.title("Segmentation Output")
plt.show()
