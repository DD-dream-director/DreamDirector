const checkMax = 3
const checkBoxes = document.getElementsByClassName('tag') // nameで取得するのではなく、class名で要素を取得するようにした.

function checkCount(target) {
    let checkCount = 0
    checkBoxes.forEach((checkBox) => {
        if (checkBoxes.checked) {
            checkCount++
        }
    })

    if (checkCount > checkMax) {
        alert('最大3つまで')
        target.checked = false
    }
}

checkBoxes.forEach((checkBox) => {
    checkBox.addEventListener('change', () => {
        checkCount(checkBox)
    })
})