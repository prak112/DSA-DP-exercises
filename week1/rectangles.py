"""
TASK

You are given three rectangles whose sides are aligned with the horizontal and vertical axes. Your task is to compute the total area covered by the rectangles. Overlapping regions are counted only once.

You may assume that all coordinates are integers in the range -10^9 ... 10^9.

Notice that going through all possible 1x1 rectangles one by one is too slow. You have to find a more efficient way to calculate the area.

Implement a function area(rec1, rec2, rec3) that returns the total area covered. The function is given three tuples, each defining one rectangle. 

Each tuple contains four integers x_1, y_1, x_2 and y_2: The top left corner is (x_1,y_1) and the bottom right corner is (x_2,y_2).
"""

def area(rec1, rec2, rec3):
  # PSEUDO
  # given information - P1(x_1, y_1)/top-left, P2(x_2, y_2)/bottom-right
  # missing information - 
    # P3(x_3, y_3), P4(x_4, y_4) and 
    # distance between P1, P3 = l, P2, P3 = b
  # Option 1 - find coordinates and calculate l,b and area
    # (x_3, y_3)/top-right = (x_2, y_1)
    # (x_4, y_4)/bottom-left = (x_1, y_2) --- not essential
    # Use Pythogoras theorem to calculate l & b-
    # distance (l) = math.sqrt((x_3 - x_1)**2 + (y_3 - y_1)**2)
    # distance (b) = math.sqrt((x_3 - x_2)**2 + (y_3 - y_2)**2)
    # calculate and return sum of all rectangles
  # Strategy flaw - does not consider Overlapping regions since they are counted twice in the current logic.

  
  import math
  
  # top-left(x_1 negX, y_1 posY), bottom-right(x_2 posX, y_2 negY) 
  # double overlap area calculation
  recs = [rec1, rec2, rec3, rec1]
  total_overlap_area = 0
  for i in range(len(recs)-1):
    max_neg_x = max(recs[i][0], recs[i + 1][0])
    min_pos_x = min(recs[i][2], recs[i + 1][2])
    min_pos_y = min(recs[i][1], recs[i + 1][1])
    max_neg_y = max(recs[i][3], recs[i + 1][3])

    # calculate overlapping rectangle region
    l = 0
    b = 0
    if max_neg_x < min_pos_x :
      l = min_pos_x - max_neg_x
    if max_neg_y < min_pos_y:
      b = min_pos_y - max_neg_y
    overlap_area = l * b
    print('overlap area : ', overlap_area)
    total_overlap_area += overlap_area
    print('total overlap area : ', total_overlap_area)

  # triple overlap area calculation
  max_neg_x = max(rec1[0], rec2[0], rec3[0])
  min_pos_x = min(rec1[2], rec2[2], rec3[2]) 
  min_pos_y = min(rec1[1], rec2[1], rec2[1])
  max_neg_y = max(rec1[3], rec2[3], rec2[3])

  # calculate overlapping rectangle region
  l = 0
  b = 0
  if max_neg_x < min_pos_x :
    l = min_pos_x - max_neg_x
  if max_neg_y < min_pos_y:
    b = min_pos_y - max_neg_y
  triple_overlap_area = l * b
  print('triple overlap area: ', triple_overlap_area)
  # total_overlap_area += triple_overlap_area
  # print('total overlap area : ', total_overlap_area)

  # individual rectangle areas
  rec1_area = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
  rec2_area = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
  rec3_area = (rec3[2] - rec3[0]) * (rec3[3] - rec3[1])
  total_area = rec1_area + rec2_area + rec3_area
  print('total area : ', total_area)

  actual_area = total_area - total_overlap_area + triple_overlap_area
  print('actual area : ', actual_area )
  return actual_area


if __name__ == "__main__":
  rec1 = (-1,1,1,-1)
  rec2 = (0,3,2,0)
  rec3 = (0,2,3,-2)
  print(area(rec1,rec2,rec3)) # 16