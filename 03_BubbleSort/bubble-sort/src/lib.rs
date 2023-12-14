// @Author: Pyi Thein Kyaw
#[derive(Debug)]
pub struct Bubble {
    list: Vec<i32>,
}

impl Bubble {
    pub fn new_list(list: Vec<i32>) -> Self {
        Bubble {list}
    }
    pub fn descending_sort(&mut self) -> &Self {

        for i in 0..self.list.len() - 1 {

            for j in i + 1 .. self.list.len() {
                if self.list[i] < self.list[j] {
                    self.list.swap(i, j);
                }
            }
        }

        self
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        // let result = add(2, 2);
        // assert_eq!(result, 4);

        let mut data_set = Bubble::new_list(
            vec![88,2,4,5,43]
        );
        data_set.descending_sort();

        assert_eq!(data_set.list, vec![88, 43, 5, 4, 2]);
    }
}
