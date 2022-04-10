import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns=3, rows=4, scale_x=30, scale_y=30, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []

        self.cut_sheet(sheet, columns, rows, scale_x, scale_y)
        self.cur_frame = 0

        self.image = self.frames[0][1]
        self.time = 0

        self.count = 0

    def cut_sheet(self, sheet, columns, rows, scale_x=50, scale_y=50):
        size = sheet.get_width(), sheet.get_height()
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            row = []
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                cut = pygame.transform.scale(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), (scale_x, scale_y))
                row.append(cut)
            self.frames.append(row)

    def update(self, x, y):
        self.count += 1
        if self.count == 2:
            self.count = 0
            return
        row = 0
        if abs(x) >= abs(y):
            if x <= 0:
                row = 1
            else:
                row = 2
        else:
            if y <= 0:
                row = 3
            else:
                row = 0
        self.cur_frame = (self.cur_frame + 1) % len(self.frames[row])
        self.image = self.frames[row][self.cur_frame]
        if not x and not y:
            self.image = self.frames[0][1]

    def get_rect(self):
        return self.image.get_rect()
