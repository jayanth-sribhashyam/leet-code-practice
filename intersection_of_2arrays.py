class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        k = 0
        list_rows = []
        while k <= numRows:
            if k==1:
                list_rows.append([1])
            if k==2:
                list_rows.append([1,1])
            if k>2:
                latest_row = list_rows[len(list_rows)-1]
                new_row = []
                new_row.append(1)
                for i in range(len(latest_row)-1):
                    new_row.append(latest_row[i]+latest_row[i+1])
                new_row.append(1)
                list_rows.append(new_row)
            k += 1
        return list_rows
        
