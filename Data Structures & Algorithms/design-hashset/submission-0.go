type MyHashSet struct {
	Value []int
}

func Constructor() MyHashSet {
	return MyHashSet{}
}

func (this *MyHashSet) Add(key int) {
    this.Value = append(this.Value,key)
}

func (this *MyHashSet) Remove(key int) {
	i := 0
	for i < len(this.Value) {
		if this.Value[i] == key {
			this.Value = append(this.Value[:i],this.Value[i+1:]...)
			i--
		}
		i++
	}
}

func (this *MyHashSet) Contains(key int) bool {
    for _, val := range this.Value {
		if val == key {
			return true
		}
	}
	return false
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
 