import cv2
import numpy as np

# Set up camera
cap = cv2.VideoCapture(0)  # Use the first available camera

# Define the lower and upper bounds for the color of the shapes you want to detect
# Replace with the lower bounds for the color
lower_color = np.array([0, 0, 0])
# Replace with the upper bounds for the color
upper_color = np.array([255, 255, 255])

# Create an empty dictionary to store the detected shapes
shapes = {}

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale and apply Gaussian blur to reduce noise
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection to find the edges of the shapes
    edges = cv2.Canny(blurred, 50, 150)

    # Find the contours of the shapes
    contours, hierarchy = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour and store the data
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)  # Get the area of the contour
        # Get the perimeter of the contour
        perimeter = cv2.arcLength(contour, True)
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Draw the bounding box and contour on the original frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.drawContours(frame, [contour], 0, (0, 0, 255), 2)

        # Store the data in the dictionary
        shape_data = {"area": area, "perimeter": perimeter,
                      "x": x, "y": y, "width": w, "height": h}
        shapes[f"shape{i+1}"] = shape_data

    # Display the original frame with the contours and bounding boxes
    cv2.imshow("Camera", frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

# Print the stored shapes
print(shapes)
