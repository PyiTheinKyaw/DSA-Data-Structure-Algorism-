use bubble_sort::Bubble;
fn main() {
    let mut bubble = Bubble::new_list(
        vec![43,1233,34,12,65,76,11]
    );

    println!("OG Bubble list: {:?}", bubble);

    bubble.descending_sort();

    println!("Sorted Bubble list: {:?}", bubble);

}