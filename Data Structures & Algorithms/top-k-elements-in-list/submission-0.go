func topKFrequent(nums []int, k int) []int {

	freq := make(map[int]int)

	// count frequencies

	for _, num := range nums {
		freq[num]++
	}

	// Create an empty min-heap

	h := &MinHeap{}
	heap.Init(h)

	for value, count := range freq { 
		heap.Push(h, Item{
			value: value,
			freq: count,
		})

		if h.Len() > k {
			heap.Pop(h)
		}
	}

	// Extract the answer 
	result := make([]int, 0, k)

	for h.Len() > 0 {
		item := heap.Pop(h).(Item)
		result = append(result, item.value)
	}
	return result

}


type Item struct {
	value int
	freq int
}

type MinHeap []Item

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i].freq < h[j].freq
}

func (h MinHeap) Swap(i, j int) { 
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x any) { 
	*h = append(*h, x.(Item))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)

	item := old[n-1]
	*h = old[:n-1]
	return item
}