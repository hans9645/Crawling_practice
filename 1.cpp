#include <iostream> 
#include <stdio.h> 
#include <stdlib.h> 
#include <stack> 
#include <algorithm> 
#include <string> 
#include <queue> 
using namespace std; 
int main(void) { 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int isvalid_n;
    string sentence;
    getline(cin, sentence);
    isvalid_n = 0; 
    stack<char> S;
    int count=0;
    int flag=0;
    
    for (auto t : sentence) { 
        count++;
        if(count==0){
            if(t=='}'||t==']'||t=='>'||t==')'){
                isvalid_n=0;
                break;
            }
        }
        if (t == '(') { 
                S.push('('); 
            } 
        else if(t=='['){
                S.push('[');
            }
        else if(t=='{'){
                S.push('{');
            }
        else if (t=='<'){
                S.push('<');
            }
        else if (t == ']') { 
            if (S.top() != '[') {
                    isvalid_n  = count*-1; 
                    break; 
                }
            else{
                flag++;  
            }
                S.pop(); 
            } 
            else if (t == ')') {
                if (S.top() != '(') { 
                    isvalid_n  = count*-1; 
                    break; 
                    } 
                else{
                flag++;  
            }
                    S.pop();
                } 
            else if (t == '>') {
                if (S.top() != '<') { 
                    isvalid_n  = count*-1; 
                    break; 
                    } 
                else{
                flag++;  
            }
                    S.pop();
                }
            else if (t == '}') {
                if (S.top() != '{') { 
                   isvalid_n  = count*-1; 
                    break; 
                    } 
                else{
                flag++;  
             }
                S.pop();
            }
        
        } 
    if(!S.empty()){
        cout<<-1*count<<'\n';
    }
    else{
        cout<<isvalid_n<<'\n';
        
    }
    return 0;
    }