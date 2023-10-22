function paramsIndividual(name: string, age: number, country: string) {
  return { name, age, country };
}

function paramsObject(params: { name: string; age: number; country: string }) {
  return params;
}
