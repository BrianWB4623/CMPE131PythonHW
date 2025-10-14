def cacti_number(plot):
    rows=len(plot)
    cols=len(plot[0])
    count=0
    for i in range(rows):
        for j in range(cols):
            if plot[i][j]==0:
                if(i>0 and plot[i-1][j]==1):
                    continue
                if(i<rows-1 and plot[i+1][j]==1):
                    continue
                if(j>0 and plot[i][j-1]==1):
                    continue
                if(j<cols-1 and plot[i][j+1]==1):
                    continue
                plot[i][j]=1
                count+=1
    return count

