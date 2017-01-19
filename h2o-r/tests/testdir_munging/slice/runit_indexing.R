setwd(normalizePath(dirname(R.utils::commandArgs(asValues=TRUE)$"f")))
source("../../../scripts/h2o-r-test-setup.R")

test.indexing = function(){
    # This function is called with a huge variety of argument styles
    # Here's the breakdown:
    #   Style          Type  #args  Description
    # df[]             - na na 2    both missing, identity with df
    # df["colname"]    - c  na 2    single column by name, df$colname
    # df[3]            - X  na 2    if ncol > 1 then column else row
    # df[,]            - na na 3    both missing, identity with df
    # df[2,]           - r  na 3    constant row, all cols
    # df[1:150,]       - r  na 3    selection of rows, all cols
    # df[,3]           - na c  3    constant column
    # df[,1:10]        - na c  3    selection of columns
    # df[,"colname"]   - na c  3    single column by name
    # df[2,"colname"]  - r  c  3    row slice and column-by-name
    # df[2,3]          - r  c  3    single element
    # df[1:150,1:10]   - r  c  3    rectangular slice
    # df[1,-1]         - r  c  3    selection of first row minus the first column
    # df[-1,-1]        - r  c  3    get rid of first row and first column
    # df[-1,1]         - r  c  3    get rid of first row and keep first column
    # df[-1:-20,-1:-3] - r  c  3    get rid of first 20 rows and first 3 columns
    # df[-1:-20,1:3]   - r  c  3    get rid of first 20 rows and keep first 3 columns
    # df[1:20,-1:-3]   - r  c  3    keep first 20 rows and remove first 3 columns
    Log.info("Upload iris dataset...")
    hf = h2o.uploadFile(locate("smalldata/iris/iris.csv"), "iris.hex")
    colnames(hf) = c("Sepal.Length", "Sepal.Width",  "Petal.Length", "Petal.Width",  "Species")

    Log.info("Setting up comparison frame in R...")
    iris = as.data.frame(hf)

    ######################################################################################
    Log.info("Test Column Indexing...")

    one_col_idx = hf[1] #Get first column
    expect_equal(one_col_idx,as.h2o(iris[1]))

    one_col_name = hf["Sepal.Length"] #Get first column by name
    expect_equal(one_col_name,as.h2o(iris["Sepal.Length"]))

    one_col_idx_cs = hf[,1] #cs = comma-separated. Get first column using comma separator
    expect_equal(one_col_idx_cs,as.h2o(iris[,1]))

    one_col_name_cs = hf[,"Sepal.Length"] #cs = comma-separated. Get first column by name and comma separator
    expect_equal(one_col_name_cs,as.h2o(iris[,"Sepal.Length"]))

    seq_col_idx_cs = hf[1:2] #Get first two columns using a sequence
    expect_equal(seq_col_idx_cs,as.h2o(iris[1:2]))

    seq_col_idx_cs = hf[,1:2] #Get first two columns using a sequence and comma separator
    expect_equal(seq_col_idx_cs,as.h2o(iris[,1:2]))

    seq_col_name = hf[,c("Sepal.Length","Sepal.Width")] #Get first two columns by name
    expect_equal(seq_col_name,as.h2o(iris[,c("Sepal.Length","Sepal.Width")]))

    neg_col_idx = hf[-1] #Get rid of first column
    expect_equal(neg_col_idx,as.h2o(iris[-1]))

    neg_col_idx_cs = hf[,-1] #cs = comma-separated. Get rid of first column using comma separator
    expect_equal(neg_col_idx_cs,as.h2o(iris[,-1]))

    seq_col_neg_idx = hf[-1:-3] #cs = comma-separated. #Get rid of first 3 columns using sequence
    expect_equal(seq_col_neg_idx,as.h2o(iris[-1:-3]))

    seq_col_neg_idx_cs = hf[,-1:-3] #cs = comma-separated. #Get rid of first 3 columns using sequence and comma separator
    expect_equal(seq_col_neg_idx_cs,as.h2o(iris[,-1:-3]))

    sequence = hf[,seq(-3,-4,-1)] #Get rid of columns 3,4 by using seq()
    expect_equal(sequence,as.h2o(iris[,seq(-3,-4,-1)]))

    sequence_v2 = hf[,seq(3,4,1)] #Get columns 3,4 by using seq()
    expect_equal(sequence_v2,as.h2o(iris[,seq(3,4,1)]))

    ######################################################################################
    Log.info("Test Row Indexing...")

    one_row_idx = hf[1,] #Get first row
    expect_equal(one_row_idx,as.h2o(iris[1,]))

    seq_row_idx = hf[1:20,] #Get first 20 rows
    expect_equal(seq_row_idx,as.h2o(iris[1,]))

    neg_row_idx = hf[-1,] #Get rid of first row
    expect_equal(neg_row_idx,as.h2o(iris[-1,]))

    neg_row_idx_cs = hf[-1:-20,] #Get rid of first 20 rows using comma separator
    expect_equal(neg_row_idx_cs,as.h2o(iris[-1:-20,]))

    sequence = hf[seq(1,40,2),]
    expect_equal(sequence, as.h2o(iris[seq(1,40,2),])) #Get rows 1,3,5,...,39

    sequence_v2 = hf[seq(-1,-40,-2),]
    expect_equal(sequence_v2, as.h2o(iris[seq(-1,-40,-2),])) #Get rows 2,4,6,...,40

    ######################################################################################
    Log.info("Test Column and Row Indexing...")

    fr1 = hf[1,-1] #Keep first row; Remove first column
    expect_equal(fr1,as.h2o(iris[1,-1]))

    fr2 = hf[1,-3] #Keep first row; Remove third column
    expect_equal(fr2,as.h2o(iris[1,-3]))

    fr3 = hf[3,-3] #Keep third row; Remove third column
    expect_equal(fr3,as.h2o(iris[3,-3]))

    fr4 = hf[3:5,-3] #Keep rows 3-5; Remove third column
    expect_equal(fr4,as.h2o(iris[3:5,-3]))

    fr5 = hf[1,c(-3,-4)] #Remove third and fourth columns
    expect_equal(fr5,as.h2o(iris[1,c(-3,-4)]))

    fr6 = hf[1,seq(-3,-4,-1)] #Remove third and fourth columns. Alternative approach
    expect_equal(fr6,as.h2o(iris[1,seq(-3,-4,-1)]))

    fr7 = hf[1:20,1:3] #Get rows 1:20 and columns 1:3
    expect_equal(fr7,as.h2o(iris[1:20,1:3]))

    fr8 = hf[-1,-1] #Remove first row; Remove first column
    expect_equal(fr8,as.h2o(iris[-1,-1]))

    fr9 = hf[-1,1] #Remove first row; Keep first column
    expect_equal(fr9,as.h2o(iris[-1,-1]))

    fr10 = hf[-1:-20,-1:-3] #Remove first 20 rows; Remove first 3 columns
    expect_equal(fr10,as.h2o(iris[-1:-20,-1:-3]))

    fr11 = hf[-1:-20,1:3] #Remove first 20 rows; Keep first 3 columns
    expect_equal(fr11,as.h2o(iris[-1:-20,1:3]))

    fr12 = hf[1:20,-1:-3] #Keep first 20 rows; Remove first 3 columns
    expect_equal(fr12,as.h2o(iris[1:20,-1:-3]))

}

doTest("Test Row & Column Indexing", test.indexing)