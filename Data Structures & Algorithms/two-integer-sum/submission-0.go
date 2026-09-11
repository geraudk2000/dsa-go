func twoSum(nums []int, target int) []int {

	seen := make(map[int]int)
	
	for index, num := range nums {

		diff := target - num 

		if previousIndex, found := seen[diff]; found {
			return []int{previousIndex, index}
		}
		seen[num] = index
	}
	return []int{}
    
}
