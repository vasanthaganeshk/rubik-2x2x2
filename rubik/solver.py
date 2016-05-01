"""
Shortest-path
Copyright (C) 2016 Vasantha Ganesh K <vasanthaganesh.k@tuta.io>.

This file is part of rubik.

This file is free software. You can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This file is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with rubik.  If not, see <http://www.gnu.org/licenses/>.
"""

import rubik
from collections import deque

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """

    frontier = deque()
    frontier.append(start)
    parent = {start: None}

    ans_found = False
    while frontier:
        u = frontier.popleft()
        if u == end:
            ans_found = True
            break
        for x in xrange(6):
            temp = rubik.perm_apply(rubik.quarter_twists[x], u)

            if temp not in parent:
                parent[temp] = x + 1 if x%2 == 0 else x - 1
                frontier.append(temp)

    ans = deque()
    if ans_found:
        m = end
        j = parent[m]
        while parent[m] != None:
            ans.appendleft(rubik.quarter_twists[j + 1 if j%2 == 0 else j - 1])
            print(rubik.quarter_twists_names[ans[0]])
            m = rubik.perm_apply(rubik.quarter_twists[j], m)
            j = parent[m]
        return list(ans)
    else:
        return None
