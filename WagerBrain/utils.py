from WagerBrain.odds import decimal_odds


def bookmaker_margin(fav_odds, dog_odds, draw_odds=None):
    """
    :param fav_odds:  The odds on offer for the favorite
    :param dog_odds:  The odds on offer for the underdog
    :return: Percentage of wager paying bookmaker margin (bookmaker's edge normalized as % in decimal terms
    """
    if not draw_odds:
        # Formula requires decimal odds
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)

        return ((1 / fav_odds) + (1 / dog_odds)) - 1

    else:
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)
        draw_odds = decimal_odds(draw_odds)

        return ((1 / fav_odds) + (1 / dog_odds) + (1 / draw_odds)) - 1


def bookmaker_commission(fav_odds, dog_odds, commish, draw_odds=None):
    """
    :param fav_odds: Market odds on favorite
    :param dog_odds: Market odds on underdog
    :param commish: Betting exchange's commission
    :param draw_odds: Market odds on a draw outcome if applicable
    :return: % representing true cost / edge to bookmaker, exchange normalized as % in decimal terms
    """
    if not draw_odds:
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)

        fav_odds = 1 + ((1 - (commish / 100)) * (fav_odds - 1))
        dog_odds = 1 + ((1 - (commish / 100)) * (dog_odds - 1))

        return (((1 / fav_odds) * 100 + (1 / dog_odds) * 100) - 100) / 100

    else:
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)
        draw_odds = decimal_odds(draw_odds)

        fav_odds = 1 + ((1 - (commish / 100)) * (fav_odds - 1))
        dog_odds = 1 + ((1 - (commish / 100)) * (dog_odds - 1))
        draw_odds = 1 + ((1 - (commish / 100)) * (draw_odds - 1))

        return (((1 / fav_odds) * 100 + (1 / dog_odds) * 100 + (1 / draw_odds) * 100) - 100) / 100
