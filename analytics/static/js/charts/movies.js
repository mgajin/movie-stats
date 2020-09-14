import { getChart } from './main.js'

$(document).ready(() => init())

$('#year-filter-form').submit((e) => {
    e.preventDefault()
    const q = $('#year-filter-form').serialize()
    const url = `/charts/months?${q}`
    ajax(url, monthsChart)
})

function init() {
    ajax('/charts/years', yearsChart)
    // ajax('/charts/months', monthsChart)
    ajax('/charts/genres', genresChart)
    ajax('/charts/genres/avg', avgRatingsChart)
    ajax('/charts/imdb?sorted=True', topRatedChart)
}

function yearsChart(response) {
    const chart = getChart(context('yearsChart'), 'line', getData(response))
}

function monthsChart(response) {
    const chart = getChart(
        context('monthsChart'),
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
