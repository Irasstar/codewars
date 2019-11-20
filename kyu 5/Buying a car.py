"""Let us begin with an example:

A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000.
He wants to keep his old car until he can buy the secondhand one.

He thinks he can save $1000 each month but the prices of his old car and
of the new one decrease of 1.5 percent per month. Furthermore this percent
of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to
make all these calculations."""

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth, i=0):

    while startPriceNew > savingperMonth * i + startPriceOld:
        return nbMonths(startPriceOld * (1 - percentLossByMonth*0.01),
                        startPriceNew * (1 - percentLossByMonth*0.01),
                        savingperMonth,
                        percentLossByMonth + 0.5 if i % 2 == 0 else percentLossByMonth,
                        i + 1
                        )
    return [i, round(startPriceOld + savingperMonth * i - startPriceNew)]

# print(nbMonths(2000, 8000, 1000, 1.5))
