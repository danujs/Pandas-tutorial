# **Merge two Data Frames
# >Arranging the rows and columns

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                 columns=cols)
df

# >Eliminate the rows of index 1 and 4 using .drop()
# >Store the data to variable df1

df1 = df.copy(deep=True)
df1 = df1.drop([1, 4])
df1

# >Eliminate the rows of index 0 and 3 using .drop()
# >Store the data to variable df2

df2 =df.copy(deep=True)
df2 =df2.drop([0, 3])
df2

# >Join the intersection data between df1 and df2 using 'inner'
df_inner = pd.merge(df1, df2, how='inner')
df_inner

# >Join all the data between df1 and df2 using 'outer'
df_outer = pd.merge(df1, df2, how='outer') #barisnya akan digabung, dimana baris adopsinya hanya diambil 1 saja
df_outer

# all the data have been merged. Completed.
