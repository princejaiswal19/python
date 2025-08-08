#include<iostream>
#include<vector>
using namespace std;
int main(){
        vector<int>nums;
        cout<<"Enter array elements:";
        for(int i=0; i<10; i++){
          int ele;
          cin>>ele;
          nums.push_back(ele);
        }
             
         for(int i=0; i<nums.size(); i++){
            cout<<nums[i]<<" ";
         }   
            cout<<endl;
        int count=0;
        int n=nums.size();
        int i=0;                        
       int j=1;
        while(i<n){
            if(nums[i+1]>nums[i]){
                 nums[j++]=nums[i+1];
                 count++;
                
            }
            i++;


            }
         for(int i=0; i<nums.size(); i++){
            cout<<nums[i]<<" ";
         }   
            
        cout<<count;
   

    return 0;
}