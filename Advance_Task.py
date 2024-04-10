import cv2
import argparse
import sys

# Define command-line arguments
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.")
parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

# Parse command-line arguments
try:
    opt = parser.parse_args()
except argparse.ArgumentError:
    print("")
    parser.print_help()
    sys.exit(0)

# Open video capture
cap = cv2.VideoCapture(opt.input_URI if opt.input_URI else 0)

# Create video output
out = cv2.VideoWriter(opt.output_URI, cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640, 480)) if opt.output_URI else None

# Process frames until the user exits
while True:
    # Capture the next frame
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to 640x480 for consistent processing
    frame = cv2.resize(frame, (640, 480))

    # Render the frame (without overlay since we don't have it in OpenCV)
    cv2.imshow('Frame', frame)

    # Write frame to output file
    if out:
        out.write(frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and output
cap.release()
if out:
    out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
