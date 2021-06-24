Jupyter 02_04 Last Checkpoint: 39 minutes ago (autosaved)

PACKAGES

Install packages
In [1]: !pip install pandas
        !pip install numpy
        !pip install scipy
        !pip install sklearn
        Import packages

In [2]: import pandas as pd
        import numpy as np
        from sklearn.preprocess import scale
        from sklearn.decomposition import PCA
        
        DATA
        Load data
        Use a filepath like for Macintosh computers.

In [3]: data = pd.read_csv('~/Desktop/b5.csv') # Mac only.

        Or use a filepath like this Windows computers. (But replace 'bart' with your own account name.)

In [ ]: data = pd.read_csv('C:/users/bart/Desktop/b5.csv') # Windows only.

        Convert data to numpy array

In [4]: X = data.values

        Scale the values

In [5]: X = scale(X)

        ANALYSIS
        
        PCA with 50 components

In [6]: pca = PCA()
        pca.fit(X)
        print(pca.explained_variance_ratio_)

        PCA with 5 components 
        
In [7]: pca5 = PCA(n_components=5)
        pca5.fit(X)
        print(pca5.explained_variance_ratio_)
        
        Contributions of variables to components
        
In [8]: print(pca5.components_)
