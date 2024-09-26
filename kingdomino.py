import cv2 as cv
import numpy as np
import os

# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"C:\Users\jonas\Desktop\Design og anvendelse af kunstig inteligens\P0\Dataset\1.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
    print(len(tiles))
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print(get_terrain(tile))
            print("=====")

# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles

# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.median(hsv_tile, axis=(0,1)) # Vi bruger median
    print(f"H: {hue}, S: {saturation}, V: {value}")

    #Vi har fundet alle værdier ved at have ekporteret alle HSV median data. Så har vi sorteret samt tilknyttede true label (det korrkete terræn) for hver tile og derefter taget mindste og højeste værdi for de intervaller for de pågældene median data for hvert Terræn
    if 22 <= hue <= 37 and 219 <= saturation <= 255 and 105 <= value <= 206:
        return "Field"
    elif 28 <= hue <= 77 and 65 <= saturation <= 225 and 25 <= value <= 70:
        return "Forrest"
    elif 34 <= hue <= 51 and 156 <= saturation <= 248 and 65 <= value <= 166:
        return "Grassland"
    elif 19 <= hue <= 105 and 34 <= saturation <= 155 and 24 <= value <= 83:
        return "Mine"
    elif 17 <= hue <= 26 and 23 <= saturation <= 181 and 73 <= value <= 143:
        return "Svamp"
    elif 104 <= hue <= 109 and 222 <= saturation <= 255 and 108 <= value <= 204:
        return "Lake"
    elif 18 <= hue <= 21 and 110 <= saturation <= 222 and 122 <= value <= 182:
        return "Table"
    return "Unknown"

if __name__ == "__main__":
    main()
