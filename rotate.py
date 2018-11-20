rotated_90_clockwise = np.rot90(img)  # rotated 90 deg once
rotated_180_clockwise = np.rot90(rotated_90_clockwise)
rotated_270_clockwise = np.rot90(rotated_180_clockwise)


cv2.imshow('Original', img)
cv2.imshow('90 deg', rotated_90_clockwise)
cv2.imshow('Inverted', rotated_180_clockwise)
cv2.imshow('270 deg', rotated_270_clockwise)

print(
" press O for to select Original \n press r for to select 90 deg \n press i for to select Inverted \n press u for to select 270 deg\n\n")
k = cv2.waitKey(0)
if (k == 111):
    cv2.destroyAllWindows()
if (k == 114):
    img = rotated_90_clockwise
if (k == 105):
    img = rotated_180_clockwise
if (k == 117):
    img = rotated_270_clockwise