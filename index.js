Ajv = require('ajv');


async function test(){
    let schemaDual = require('./data/schemas/dual.json');
    let schemaDualCond = require('./data/schemas/dual-conditional.json');
    let schemaSingle = require('./data/schemas/single.json');
    let testFile = require('./data/to_validate/test.json');
    const ajv = new Ajv();

    validatorDual = ajv.compile(schemaDual);
    validatorDualCond = ajv.compile(schemaDualCond);
    validatorSingle = ajv.compile(schemaSingle);

    validatorDual(testFile);
    validatorDualCond(testFile);
    validatorSingle(testFile);

    validatorSingle.errors.forEach(error => {
        console.log("Error for single schema: ", error.instancePath, " ", error.message)
    });
    validatorDual.errors.forEach(error => {
        console.log("Error for dual schema: ", error.instancePath, " ", error.message)
    });
    validatorDualCond.errors.forEach(error => {
        console.log("Error for dual conditional schema: ", error.instancePath, " ", error.message)
    });
}

test();
