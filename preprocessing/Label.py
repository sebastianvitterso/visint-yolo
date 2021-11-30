SIZE = (1280, 720)

categories = ['traffic sign', 'traffic light', 'car', 'rider', 'motorcycle', 'pedestrian', 'bus', 'truck', 'bicycle', 'other vehicle', 'train', 'trailer', 'other person']

class Label():
    def __init__(self, top:int, bottom:int, left:int, right:int, category:int):
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left
        self.category = category
        
    def __str__(self):
        return f"<Label category={self.category}, top={self.top}, bottom={self.bottom}, left={self.left}, right={self.right}>"
    def __repr__(self):
        return self.__str__()

    @classmethod
    def fromJsonBbox(cls, bbox:dict):
        try:
            category_index = categories.index(bbox['category'])
        except:
            categories.append(bbox['category'])
            category_index = categories.index(bbox['category'])

        top     = int(bbox['box2d']['y1'])
        bottom  = int(bbox['box2d']['y2'])
        left    = int(bbox['box2d']['x1'])
        right   = int(bbox['box2d']['x2'])

        return Label(top, bottom, left, right, category_index)

    @classmethod
    def fromLabelLine(cls, label_line:str):
        ''' label_line should look something like `0 0.546844181459566 0.53125 0.008382642998027613 0.013157894736842105` '''
        tokens = label_line.split(' ')
        category, center_x_relative, center_y_relative, width_relative, height_relative = int(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3]), float(tokens[4])

        # Explanation inside and outward:
        # 1. Transform from center-position to edge-position:   a = (center_x_relative - (width_relative  / 2))
        # 2. Transform from relative to pixel-position:         b = SIZE[0] * a
        # 3. Transform from float to int:                       c = int(b)
        # 4. Make sure the value doesn't go outside the SIZE:   d = max(c, 0)
        left =   max(int(SIZE[0] * (center_x_relative - (width_relative  / 2))), 0)
        right =  min(int(SIZE[0] * (center_x_relative + (width_relative  / 2))), SIZE[0] - 1)
        top =    max(int(SIZE[1] * (center_y_relative - (height_relative / 2))), 0)
        bottom = min(int(SIZE[1] * (center_y_relative + (height_relative / 2))), SIZE[1] - 1)

        return cls(top, bottom, left, right, category)

    def toLabelLine(self):
        center_x_px = (self.left + self.right) / 2
        center_y_px = (self.top + self.bottom) / 2
        center_x_relative = center_x_px / SIZE[0]
        center_y_relative = center_y_px / SIZE[1]

        width_px = (self.right - self.left)
        height_px = (self.bottom - self.top)
        width_relative = width_px / SIZE[0]
        height_relative = height_px / SIZE[1]

        assert center_x_relative + (width_relative / 2) <= 1, 'Boundingbox crossing edge: RIGHT'
        assert center_x_relative - (width_relative / 2) >= 0, 'Boundingbox crossing edge: LEFT'
        assert center_y_relative + (height_relative / 2) <= 1, 'Boundingbox crossing edge: BOTTOM'
        assert center_y_relative - (height_relative / 2) >= 0, 'Boundingbox crossing edge: TOP'

        return f"{self.category} {center_x_relative} {center_y_relative} {width_relative} {height_relative}"

    def area(self):
        height = self.bottom - self.top
        width = self.right - self.left
        return height*width

