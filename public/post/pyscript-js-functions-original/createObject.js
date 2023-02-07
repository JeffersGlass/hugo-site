function createObject(x, variableName){
    let execString = variableName + " = x"
    console.log("Running `" + execString + "`");
    eval(variableName + " = x")
}