var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const setInt = new Set(nums2.filter(n => set1.has(n)));
    return [...setInt]
};