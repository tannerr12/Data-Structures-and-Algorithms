impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let mut res = f64::MIN;
        let mut prefix = vec![0];
        for &num in &nums {
            prefix.push(*prefix.last().unwrap() + num);
        }

        for i in k as usize..=nums.len() {
            let mut l = 0;
            let mut r = i;
            while r < prefix.len() {
                res = res.max((prefix[r] as f64 - prefix[l] as f64) / i as f64);

                l += 1;
                r += 1;
            }
        }
        res
}

    
}