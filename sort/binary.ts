let numList = [1, 2, 4, 5, 6, 7, 9, 12, 32, 38, 50, 70, 81, 92, 200, 212,]

function binarySearch(list: number[], goal: number) {
    let start = 0, end = list.length - 1
    while (start <= end) {
        let mid = Math.floor((start + end) / 2)
        if (list[mid] === goal) {
            return mid
        }
        else {
            if (list[mid] < goal) {
                start = mid + 1
            } else {
                end = mid - 1
            }
        }
    }
    return false
}

console.log(binarySearch(numList, 38))