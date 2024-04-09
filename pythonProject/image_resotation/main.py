import cv2

# Read the degraded image
degraded_image_path = "wallpaperflare.com_wallpaper (1).jpg"
degraded_image = cv2.imread(degraded_image_path)

# Check if the image is successfully loaded
if degraded_image is None:
    print("Error: Unable to load the image.")
else:
    print("Degraded image loaded successfully.")

    # Apply Gaussian blur filter for image restoration
    restored_image = cv2.GaussianBlur(degraded_image, (5, 5), 0)

    # Display the degraded and restored images (optional)
    cv2.imshow("Degraded Image", degraded_image)
    cv2.imshow("Restored Image", restored_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the restored image
    restored_image_path = "restored_image.jpg"
    cv2.imwrite(restored_image_path, restored_image)

    print("Restored image saved successfully as", restored_image_path)
