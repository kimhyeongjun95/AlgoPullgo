//
//  main.cpp
//  Baekjun_cp
//
//  Created by woosteel on 01/08/2019.
//  Copyright © 2019 woosteel. All rights reserved.
//
#include <stdio.h>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int dice[6] = {0, 0, 0, 0, 0, 0};

void north()
{ //북쪽으로 이동
    int temp = dice[2];
    dice[2] = dice[0];
    dice[0] = dice[5];
    dice[5] = dice[4];
    dice[4] = temp;
}

void south()
{ //남쪽으로 이동
    int temp = dice[2];
    dice[2] = dice[4];
    dice[4] = dice[5];
    dice[5] = dice[0];
    dice[0] = temp;
}

void east()
{ //동쪽으로 이동
    int temp = dice[2];
    dice[2] = dice[3];
    dice[3] = dice[5];
    dice[5] = dice[1];
    dice[1] = temp;
}

void west()
{ //서쪽으로 이동
    int temp = dice[2];
    dice[2] = dice[1];
    dice[1] = dice[5];
    dice[5] = dice[3];
    dice[3] = temp;
}

int main()
{
    int n, m;
    int x, y;
    int k;
    scanf("%d %d %d %d %d", &n, &m, &x, &y, &k);

    int map[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            scanf("%d", &map[i][j]); //지도정보 저장
    }

    dice[5] = map[x][y];

    int dir; //방향정보
    for (int i = 0; i < k; i++)
    {
        scanf("%d", &dir);
        if (dir == 1)
        {
            if ((y + 1) > (m - 1))
                continue;
            else
            {
                y++;
                east();

                if (map[x][y] == 0)
                    map[x][y] = dice[2];

                else
                {
                    dice[2] = map[x][y];
                    map[x][y] = 0;
                }
                printf("%d\n", dice[5]);
            }
        }

        else if (dir == 2)
        {
            if ((y - 1) < 0)
                continue;
            else
            {
                y--;
                west();

                if (map[x][y] == 0)
                    map[x][y] = dice[2];

                else
                {
                    dice[2] = map[x][y];
                    map[x][y] = 0;
                }
                printf("%d\n", dice[5]);
            }
        }

        else if (dir == 3)
        {
            if ((x - 1) < 0)
                continue;
            else
            {
                x--;
                north();

                if (map[x][y] == 0)
                    map[x][y] = dice[2];

                else
                {
                    dice[2] = map[x][y];
                    map[x][y] = 0;
                }
                printf("%d\n", dice[5]);
            }
        }

        else if (dir == 4)
        {
            if ((x + 1) > (n - 1))
                continue;
            else
            {
                x++;
                south();

                if (map[x][y] == 0)
                    map[x][y] = dice[2];

                else
                {
                    dice[2] = map[x][y];
                    map[x][y] = 0;
                }
                printf("%d\n", dice[5]);
            }
        }

        else
            continue;
    }
}
