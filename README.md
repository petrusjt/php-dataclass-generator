# php-dataclass-generator

## Description

This script generates a php data class from command line arguments

# Usage

```bash
    python generate_dataclass_php.py <ClassName> [fields]
```

# Example

The following  

```bash
    python generate_dataclass_php.py Test id name age
```  
generates:

```php
<?php

class Test
{
	private $id;
	private $name;
	private $age;

	//Konstruktor null alapértelmezett paraméterekkel

	public function __construct($id=null, $name=null, $age=null)
	{
		$this->id = $id;
		$this->name = $name;
		$this->age = $age;
	}

	//Getterek/Setterek

    public function getId()
    {
        return $this->id;
    }
    public function setId($id)
    {
        $this->id = $id;
    }
        
    public function getName()
    {
        return $this->name;
    }
    public function setName($name)
    {
        $this->name = $name;
    }
        
    public function getAge()
    {
        return $this->age;
    }
    public function setAge($age)
    {
        $this->age = $age;
    }
        
	//Builder pattern-szerűség

    public function Id($id)
    {
        $this->id = $id;
    }

    public function Name($name)
    {
        $this->name = $name;
    }

    public function Age($age)
    {
        $this->age = $age;
    }
}
?>
```

int the file Test.php
