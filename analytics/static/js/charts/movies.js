import { getChart } from './main.js'

$(document).ready(() => init())

function init() {
    ajax('/charts/months', dateChart)
    ajax('/charts/genres', genresChart)
    ajax('/charts/genres/avg', avgRatingsChart)
    ajax('/charts/imdb?sorted=True', topRatedChart)
}

function dateChart(response) {
    const chart = getChart(
        context('releasedChart'),
        'verticalBar',
        getData(response)
    )
}

function genresChart(response) {
    const chart = getChart(context('genresChart'), 'pie', getData(response))
}

const avgRatingsChart = (response) => {
    const chart = getChart(
        context('avgRatingsChart'),
        'verticalBar',
        getData(response)
    )
}

const topRatedChart = (response) => {
    const chart = getChart(
        context('ratingsChart'),
        'horizontalBar',
        getData(response)
    )
}

const ajax = (endpoint, func) => {
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: (response) => func(response),
        error: (error) => alert(error.message),
    })
}

const getData = (response) => {
    return { data: response.data, labels: response.labels }
}

const context = (id) => {
    return document.getElementById(id).getContext('2d')
}
