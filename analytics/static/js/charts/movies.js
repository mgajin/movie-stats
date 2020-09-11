import { getChart } from './main.js'

$(document).ready(() => {
    const endpoint = '/charts/imdb?sorted=True'
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: (response) => init(response),
        error: (error) => {
            alert('Error')
        },
    })
})

const init = (response) => {
    const { data, labels } = response
    const chartData = { data, labels }
    const ctx = document.getElementById('ratingsChart').getContext('2d')
    const chart = getChart(ctx, 'horizontalBar', chartData)
}
