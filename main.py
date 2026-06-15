def classify_image(image_name):
    labels = [
        "Cat",
        "Dog",
        "Car",
        "Person"
    ]

    prediction = labels[0]

    return {
        "image": image_name,
        "prediction": prediction
    }

result = classify_image("sample.jpg")
print(result)
