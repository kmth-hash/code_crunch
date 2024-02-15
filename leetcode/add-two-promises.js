// https://leetcode.com/problems/add-two-promises/description/

var addTwoPromises = async function(promise1, promise2) {

    let [v1, v2] = await Promise.all([promise1, promise2]);
  
    return v1 + v2;
  };