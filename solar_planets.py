import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol   (UwU)",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            2,
            (0,0,255))

cv2.putText(img,
            "Mercurio",
            (110,180),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (190,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Tierra",
            (300,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Marte",
            (400,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (590,60),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturno",
            (720,110),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Urano",
            (950,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptuno",
            (1100,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.imshow ("PRO-C104: NOMBRA LOS PLANETAS", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)