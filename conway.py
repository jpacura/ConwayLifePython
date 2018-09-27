class Conway:
    def __init__(self, x, y):
        self.currentField = [[False for x in range(y)] for x in range(x)]
        self.tempField    = [[False for x in range(y)] for x in range(x)]
        self.time = 0

    def is_alive(self, x, y):
        return self.currentField[x][y]

    def tick(self):
        for i in range(0, len(self.currentField)):
            for j in range(0, len(self.currentField[i])):
                living_neighbors = self.count_living_neighbors(i, j)
                # Assign new value to temporary field to not mess up current value for other iterations
                
                if self.is_alive(i, j):
                    # Cell is alive
                    if living_neighbors == 2 or living_neighbors == 3:
                        # Cell will live
                        self.tempField[i][j] = True
                    else:
                        # Cell will die
                        self.tempField[i][j] = False
                else:
                    # Cell is dead
                    if living_neighbors == 3:
                        # Cell will come back to life
                        self.tempField[i][j] = True
                    else:
                        # Cell will remain dead
                        self.tempField[i][j] = False

        # Switch the two fields after calculating new state
        self.currentField, self.tempField = self.tempField, self.currentField
        self.time += 1

    
    def count_living_neighbors(self, x, y):
        count = 0

        xlen = len(self.currentField) - 1
        ylen = len(self.currentField[x]) - 1

        if x > 0 and y > 0:
            count = count + self.is_alive(x - 1, y - 1)

        if x > 0:
            count = count + self.is_alive(x - 1, y)

        if x > 0 and y < ylen:
            count = count + self.is_alive(x - 1, y + 1)

        if x < xlen and y > 0:
            count = count + self.is_alive(x + 1, y - 1)

        if x < xlen:
            count = count + self.is_alive(x + 1, y)

        if x < xlen and y < ylen:
            count = count + self.is_alive(x + 1, y + 1)

        if y > 0:
            count = count + self.is_alive(x, y - 1)

        if y < ylen:
            count = count + self.is_alive(x, y + 1)

        return count
