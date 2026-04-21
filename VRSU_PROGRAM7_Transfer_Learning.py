import tensorflow as tf
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np

# Load pretrained model
base_model = MobileNet(weights='imagenet', include_top=False)

# Freeze layers
for layer in base_model.layers:
    layer.trainable = False

# Add classifier
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(5, activation='softmax')
])

model.compile(optimizer=Adam(),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Dummy data
x = np.random.rand(10, 224, 224, 3)
y = tf.keras.utils.to_categorical(np.random.randint(5, size=10), 5)

# Train
model.fit(x, y, epochs=1)

print("Model trained successfully")
