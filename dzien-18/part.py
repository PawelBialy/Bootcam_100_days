import colorgram

new_rgb_color = []

colors = colorgram.extract('image.jpg', 20)

for color in colors :
    r = color.rgb.r
    g = color.rgb.g
    b =color.rgb.b
    new_color = (r, g ,b)
    new_rgb_color.append(new_color)
print(new_rgb_color)

new_list_color = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189),
                  (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16),
                  (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]
