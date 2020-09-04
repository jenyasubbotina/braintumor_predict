import yaml
import pandas as pd
from ludwig.api import LudwigModel

train = pd.read_csv("brain_tumor_train.csv")
test = pd.read_csv("brain_tumor_test.csv")
validation = pd.read_csv("brain_tumor_validation.csv")

model_definition = {
    "input_features":
        [
            {"name": "image_path", "type": "image", "encoder": "stacked_cnn", "preprocessing":

                {"resize_method": "crop_or_pad", "width": 240, "height": 240}
             }
        ],
    "output_features":
        [
            {"name": "label", "type": "category"}
        ],
    "training":

        {"batch_size": 8, "epochs": 5}
}

model = LudwigModel(model_definition)
train_stats = model.train(data_train_df=train, data_test_df=test)
predictions = model.predict(data_df=validation)
model.save("C:/Users/WINDOWS 10/PycharmProjects/brain_tumor/ludwig_model")
model.close()
