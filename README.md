# Corn-Disease-Detection

The project aims to help primary industries, specifically for the farms that producing corns, detect the what type of disease that racks their corn yield also assist the farmers finding out the information about the disease as well as the treatments with which they to take action.

## **Data Overview**

In the [data](https://universe.roboflow.com/corn-disease-7/corn-diseases-oxojk/dataset/2) from roboflow there are 3 types of diseases we chose for our classification such as `Corn Rust`, `Grey Leaf Spot`, `Leaf Blight`.

So let's see the picturer of the all diseases:

**Corn Rust**

<img src="assets\images\Corn Rust.png" alt="Corn Rust Disease" width="300"/>

**Grey Leaf Spot**

<img src="assets\images\Gray Leaf Spot.png" alt="Corn Rust Disease" width="300"/>

**Leaf Blight**

<img src="assets\images\Corn Leaf Blight.png" alt="Corn Rust Disease" width="300"/>

### **Data Preparation**

The data used in this project underwent several preprocessing steps to ensure optimal model performance:

1. **Data Collection**: Images were sourced from Roboflow's dataset, containing three main corn disease categories.

2. **Image Preprocessing**:
    - Resized to uniform dimensions (640x640 pixels)
    - Normalized pixel values
    - Applied augmentation techniques:
      - Random rotation
      - Horizontal flip
      - Brightness adjustment
      - Contrast enhancement

3. **Dataset Split**:
    - Training set: 70%
    - Validation set: 15%
    - Test set: 15%

4. **Label Encoding**: 
    we used `dummy` method for categorical disease labels:
    - Corn Rust: [1, 0, 0]
    - Grey Leaf Spot: [0, 1, 0]
    - Leaf Blight: [0, 0, 1]
    On problem is that the data is in form of `image` which is not possible the do as said, but fortunately the we have a `csv` file for each data that classifies the class for each image:
    <br>
    <img src="assets\images\classification.png" alt="Corn Rust Disease" width="500"/>



#### **1. Drawbacks of Original Data**

## References

[Corn Rust from Menisota University](https://ohioline.osu.edu/factsheet/plpath-cer-02)

[Gray leaf spot on corn from Menisota University](https://extension.umn.edu/corn-pest-management/gray-leaf-spot-corn)

[Corn Leaf Blight from Menisota University](https://extension.umn.edu/corn-pest-management/northern-corn-leaf-blight)