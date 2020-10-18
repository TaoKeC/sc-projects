"""
File: 
Name: TAO-KE CHORNG
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    《Retro Cyberpunk Taipei 2033》
    This image shows an imagination of a future Taipei as a high-tech city. The author create this image
    by using 80's retro sci-fi style with vector elements to create it.
    """
    window = GWindow(600, 500, title='Retro Cyberpunk Taipei 2033')

    # background elements
    background = GRect(600, 500)
    background.filled = True
    window.add(background)

    moon = GOval(300, 300)
    moon.color = 'white'
    moon.filled = True
    moon.fill_color = 'white'
    moon_x = (background.width - moon.width)/2
    moon_y = (background.height - moon.height)/2
    window.add(moon, moon_x, moon_y)

    # mountain
    mountain = GPolygon()
    mountain.add_vertex((0, 600))
    mountain.add_vertex((0, 200))
    mountain.add_vertex((100, 470))
    mountain.add_vertex((220, 310))
    mountain.add_vertex((320, 380))
    mountain.add_vertex((420, 280))
    mountain.add_vertex((435, 295))
    mountain.add_vertex((465, 260))
    mountain.add_vertex((550, 400))
    mountain.add_vertex((600, 200))
    mountain.add_vertex((600, 500))
    mountain.color = 'mediumpurple'
    mountain.filled = True
    mountain.fill_color = 'mediumpurple'
    window.add(mountain)

    mountain2 = GPolygon()
    mountain2.add_vertex((0, 600))
    mountain2.add_vertex((0, 400))
    mountain2.add_vertex((80, 280))
    mountain2.add_vertex((110, 320))
    mountain2.add_vertex((130, 300))
    mountain2.add_vertex((230, 420))
    mountain2.add_vertex((310, 300))
    mountain2.add_vertex((400, 400))
    mountain2.add_vertex((460, 330))
    mountain2.add_vertex((490, 360))
    mountain2.add_vertex((520, 300))
    mountain2.add_vertex((600, 400))
    mountain2.add_vertex((600, 500))
    mountain2.color = 'violet'
    mountain2.filled = True
    mountain2.fill_color = 'violet'
    window.add(mountain2)

    building5 = GRect(45, 160)
    building5.color = 'lightsteelblue'
    building5.filled = True
    building5.fill_color = 'lightsteelblue'
    window.add(building5, 285, 500 - building5.height)

    building6 = GRect(70, 105)
    building6.color = 'lightsteelblue'
    building6.filled = True
    building6.fill_color = 'lightsteelblue'
    window.add(building6, 320, 500 - building6.height)

    building7 = GRect(45, 130)
    building7.color = 'lightsteelblue'
    building7.filled = True
    building7.fill_color = 'lightsteelblue'
    window.add(building7, 90, 500 - building7.height)

    building4 = GPolygon()
    building4.add_vertex((260, 500))
    building4.add_vertex((260, 110))
    building4.add_vertex((290, 130))
    building4.add_vertex((290, 500))
    building4.color = 'cornflowerblue'
    building4.filled = True
    building4.fill_color = 'cornflowerblue'
    window.add(building4)

    building4_1 = GRect(20, 245)
    building4_1.color = 'cornflowerblue'
    building4_1.filled = True
    building4_1.fill_color = 'cornflowerblue'
    window.add(building4_1, 240, window.height - building4_1.height)

    building4_2 = GRect(20, 145)
    building4_2.color = 'cornflowerblue'
    building4_2.filled = True
    building4_2.fill_color = 'cornflowerblue'
    window.add(building4_2, 290, window.height - building4_2.height)

    building2 = GRect(70, 305)
    building2.color = 'cornflowerblue'
    building2.filled = True
    building2.fill_color = 'cornflowerblue'
    window.add(building2, 120, 500 - building2.height)

    windows1 = GRect(60, 40)
    windows1.color = 'lightskyblue'
    windows1.filled = True
    windows1.fill_color = 'lightskyblue'
    window.add(windows1, 125, 500 - windows1.height - 10)

    windows2 = GRect(60, 40)
    windows2.color = 'lightskyblue'
    windows2.filled = True
    windows2.fill_color = 'lightskyblue'
    window.add(windows2, 125, 500 - 100)

    windows3 = GRect(60, 40)
    windows3.color = 'lightskyblue'
    windows3.filled = True
    windows3.fill_color = 'lightskyblue'
    window.add(windows3, 125, 500 - 150)

    windows4 = GRect(60, 40)
    windows4.color = 'lightskyblue'
    windows4.filled = True
    windows4.fill_color = 'lightskyblue'
    window.add(windows4, 125, 500 - 200)

    windows5 = GRect(60, 40)
    windows5.color = 'lightskyblue'
    windows5.filled = True
    windows5.fill_color = 'lightskyblue'
    window.add(windows5, 125, 500 - 250)

    windows6 = GRect(60, 40)
    windows6.color = 'lightskyblue'
    windows6.filled = True
    windows6.fill_color = 'lightskyblue'
    window.add(windows6, 125, 500 - 300)

    building3_floor = GRect(60, 120)
    building3_floor.color = 'cornflowerblue'
    building3_floor.filled = True
    building3_floor.fill_color = 'cornflowerblue'
    window.add(building3_floor, 375, 500 - building3_floor.height)

    building3_middle = GRect(40, 170)
    building3_middle.color = 'cornflowerblue'
    building3_middle.filled = True
    building3_middle.fill_color = 'cornflowerblue'
    window.add(building3_middle, 385, 500 - building3_floor.height - building3_middle.height)

    building3_top = GRect(20, 10)
    building3_top.color = 'cornflowerblue'
    building3_top.filled = True
    building3_top.fill_color = 'cornflowerblue'
    window.add(building3_top, 395, 500 - building3_floor.height - building3_middle.height - building3_top.height)

    building3_aerial = GRect(2, 120)
    building3_aerial.color = 'cornflowerblue'
    building3_aerial.filled = True
    building3_aerial.fill_color = 'cornflowerblue'
    window.add(building3_aerial, 404, 500 - building3_floor.height - building3_middle.height - building3_aerial.height)

    building1 = GRect(110, 95)
    building1.color = 'royalblue'
    building1.filled = True
    building1.fill_color = 'royalblue'
    window.add(building1, 155, 500 - building1.height)

    building1_1 = GRect(90, 10)
    building1_1.color = 'royalblue'
    building1_1.filled = True
    building1_1.fill_color = 'royalblue'
    window.add(building1_1, 165, 500 - building1.height - building1_1.height)

    building1_p = GPolygon()
    building1_p.add_vertex((175, 395))
    building1_p.add_vertex((245, 395))
    building1_p.add_vertex((210, 335))
    building1_p.color = 'royalblue'
    building1_p.filled = True
    building1_p.fill_color = 'royalblue'
    window.add(building1_p)

    building101 = GPolygon()
    building101.add_vertex((320, 500))
    building101.add_vertex((330, 440))
    building101.add_vertex((360, 440))
    building101.add_vertex((370, 500))
    building101.color = 'royalblue'
    building101.filled = True
    building101.fill_color = 'royalblue'
    window.add(building101)

    b101_2 = GPolygon()
    b101_2.add_vertex((330, 440))
    b101_2.add_vertex((325, 410))
    b101_2.add_vertex((365, 410))
    b101_2.add_vertex((360, 440))
    b101_2.color = 'royalblue'
    b101_2.filled = True
    b101_2.fill_color = 'royalblue'
    window.add(b101_2)

    b101_3 = GPolygon()
    b101_3.add_vertex((330, 410))
    b101_3.add_vertex((325, 380))
    b101_3.add_vertex((365, 380))
    b101_3.add_vertex((360, 410))
    b101_3.color = 'royalblue'
    b101_3.filled = True
    b101_3.fill_color = 'royalblue'
    window.add(b101_3)

    b101_4 = GPolygon()
    b101_4.add_vertex((330, 380))
    b101_4.add_vertex((325, 350))
    b101_4.add_vertex((365, 350))
    b101_4.add_vertex((360, 380))
    b101_4.color = 'royalblue'
    b101_4.filled = True
    b101_4.fill_color = 'royalblue'
    window.add(b101_4)

    b101_5 = GPolygon()
    b101_5.add_vertex((330, 350))
    b101_5.add_vertex((325, 320))
    b101_5.add_vertex((365, 320))
    b101_5.add_vertex((360, 350))
    b101_5.color = 'royalblue'
    b101_5.filled = True
    b101_5.fill_color = 'royalblue'
    window.add(b101_5)

    b101_r = GRect(30, 5)
    b101_r.color = 'royalblue'
    b101_r.filled = True
    b101_r.fill_color = 'royalblue'
    window.add(b101_r, 330, 315)

    b101_6 = GPolygon()
    b101_6.add_vertex((340, 315))
    b101_6.add_vertex((337, 295))
    b101_6.add_vertex((355, 295))
    b101_6.add_vertex((352, 315))
    b101_6.color = 'royalblue'
    b101_6.filled = True
    b101_6.fill_color = 'royalblue'
    window.add(b101_6)

    b101_7 = GRect(2, 30)
    b101_7.color = 'royalblue'
    b101_7.filled = True
    b101_7.fill_color = 'royalblue'
    window.add(b101_7, 345, 265)

    building8 = GRect(95, 40)
    building8.color = 'lightskyblue'
    building8.filled = True
    building8.fill_color = 'lightskyblue'
    window.add(building8, 220, 500 - building8.height)

    # br = GPolygon()
    # br.add_vertex((250, 500))
    # br.add_vertex((250, 450))
    # br.add_vertex((300, 500))
    # br.color = 'lightskyblue'
    # br.filled = True
    # br.fill_color = 'lightskyblue'
    # window.add(br)

    building6 = GPolygon()
    building6.add_vertex((350, 500))
    building6.add_vertex((350, 475))
    building6.add_vertex((405, 475))
    building6.add_vertex((445, 435))
    building6.add_vertex((485, 475))
    building6.add_vertex((485, 500))
    building6.color = 'lightskyblue'
    building6.filled = True
    building6.fill_color = 'lightskyblue'
    window.add(building6)

    # stars
    star1 = GOval(4, 1)
    star1.color = 'white'
    star1.filled = True
    star1.fill_color = 'white'
    window.add(star1, 50, 50)

    star2 = GOval(1, 2)
    star2.color = 'white'
    star2.filled = True
    star2.fill_color = 'white'
    window.add(star2, 150, 30)

    star3 = GOval(1, 1)
    star3.color = 'white'
    star3.filled = True
    star3.fill_color = 'white'
    window.add(star3, 300, 70)

    star4 = GRect(2, 2)
    star4.color = 'white'
    star4.filled = True
    star4.fill_color = 'white'
    window.add(star4, 350, 20)

    star5 = GOval(2, 1)
    star5.color = 'white'
    star5.filled = True
    star5.fill_color = 'white'
    window.add(star5, 75, 240)

    star6 = GRect(2, 1)
    star6.color = 'white'
    star6.filled = True
    star6.fill_color = 'white'
    window.add(star6, 110, 120)

    star7 = GRect(1, 3)
    star7.color = 'white'
    star7.filled = True
    star7.fill_color = 'white'
    window.add(star7, 550, 120)

    star8 = GOval(1, 1)
    star8.color = 'white'
    star8.filled = True
    star8.fill_color = 'white'
    window.add(star8, 480, 40)

    star9 = GRect(1, 1)
    star9.color = 'white'
    star9.filled = True
    star9.fill_color = 'white'
    window.add(star9, 500, 220)

    # label
    label = GLabel('stanCode')
    label.color = 'ivory'
    label.font = 'Helvetica-8'
    window.add(label, 330, 362)


if __name__ == '__main__':
    main()
