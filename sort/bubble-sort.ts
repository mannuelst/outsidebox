let array = [3, 42, 2, 65]


function bubbleSort(numList: number[]) {

    let swapped: boolean
    do {
        swapped = false
        for (let i = 0; i < (numList.length - 1); i++) {
            if (numList[i] > numList[i + 1]) {
                let aux = numList[i]
                numList[i] = numList[i + 1]
                numList[i + 1] = aux

                swapped = true //se teve mudança ou troca!!
            }

        }


    } while (swapped)

    return numList
}

console.log(bubbleSort(array))