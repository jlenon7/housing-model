# Housing Model 🤖

> Model that predicts what will be the price of a housing based on the number of bedrooms, bathrooms, square footage, etc.

[![GitHub followers](https://img.shields.io/github/followers/jlenon7.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/jlenon7?tab=followers)
[![GitHub stars](https://img.shields.io/github/stars/jlenon7/housing-model.svg?style=social&label=Star&maxAge=2592000)](https://github.com/jlenon7/housing-model/stargazers/)

<p>
    <a href="https://www.buymeacoffee.com/athenna" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</p>

## Results

> Verify that train/test data is being over fitting:

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
