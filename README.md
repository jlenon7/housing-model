# Housing Model 🤖

> Model that predicts what will be the price of a housing based on the number of bedrooms, bathrooms, square footage, etc.

## Results

> Verify that train/test data is not over fitting:
<img src="storage/plots/model/is-overfitting-train-test-data.png" width="500px">

> Real prices vs predictions done by the model:
<img src="storage/plots/model/predictions.png" width="500px">

## Train/Test data analytics

> Count how many data we have with determined number of bedrooms
<img src="storage/plots/dataframe/c-bedrooms.png" width="500px">

> Price distribution in **King County** city. This plot has been created
> by using the `lat` and `long` fields to create the map of the city.
> Greener values mean higher prices, redder means cheaper.
<img src="storage/plots/dataframe/pd-king-county.png" width="500px">

> Price distribution by the number of bedrooms:
<img src="storage/plots/dataframe/pd-per-bedrooms.png" width="500px">

> Price distribution by month:
<img src="storage/plots/dataframe/pd-per-month.png" width="500px">

> Price distribution by year:
<img src="storage/plots/dataframe/pd-per-year.png" width="500px">

> Price distribution by if the house/apartment is waterfront or not:
<img src="storage/plots/dataframe/pd-per-waterfront.png" width="500px">

## Running

To run the model first create a new Python environment and activate it. I'm using [Anaconda](https://www.anaconda.com/) for that:

```shell
conda create -n housing_env python=3.11
conda activate housing_env
```

Now install all the project dependencies:

```shell
make install-all
```

And run the model:

```shell
make model
```

After running you model, it will be saved inside `storage/housing-model.keras`.
To just run your recent created model and predict a random value from our data set,
use the following script:

```shell
make predict 
```

Remember that for this to work, you need to run `make model` first to create your model.
