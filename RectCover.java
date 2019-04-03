public class Solution {
    public int RectCover(int target) {
        if (target<=0){
            return 0;
        }

        if (target<=2){
            return target;
        }
        else {
            return RectCover(target-1)+RectCover(target-2);
        }
    }
}
