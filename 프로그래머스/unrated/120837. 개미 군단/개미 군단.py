def solution(hp):
    rook = 5
    knight = 3
    pawn = 1
    count =0
    rook_num = hp // rook
    hp -= rook_num * rook
    
    knight_num = hp // knight
    hp -= knight_num * knight
    
    return rook_num + knight_num + hp
    
    
    # while (hp):
    #     if hp < rook:
    #         if hp < knight:
    #             hp -= pawn
    #             count += 1
    #         hp -= knight
    #         count += 1
    #     hp -= rook
    #     count += 1
    return count