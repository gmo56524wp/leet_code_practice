class Solution {
public:
    bool isValid(string s) {
        stack<char> Stack;
        Stack.push(s.at(0));
        for (int i = 1; i < s.length(); i++){
            if (s.at(i) == '(' || s.at(i) == '[' || s.at(i) == '{'){
                Stack.push(s.at(i));
            }else{
                if (Stack.empty() == true){
                    return false;
                }else{
                    switch(s.at(i)){
                        case ')':
                            if (Stack.top() == '('){
                                Stack.pop();
                                break;
                            }else return false;
                        case ']':
                            if (Stack.top() == '['){
                                Stack.pop();
                                break;
                            }else return false;
                        case '}':
                            if (Stack.top() == '{'){
                                Stack.pop();
                                break;
                            }else return false;
                    }
                }
            }
        }
        if (Stack.empty() == true) return true;
            else return false;
    }
};